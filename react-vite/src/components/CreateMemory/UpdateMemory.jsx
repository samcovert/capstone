import { Fragment, useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from "react-router-dom"
import { fetchAddImage, fetchEditMemory, fetchOneMemory } from "../../redux/memories"
import { fetchEditImage } from "../../redux/merch"


const UpdateMemory = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    let { memoryId } = useParams()
    memoryId = +memoryId
    const memory = useSelector(state => state.memories[memoryId])
    const [title, setTitle] = useState('')
    const [details, setDetails] = useState('')
    const [ogUrls, setOgUrls] = useState([])
    const [newUrls, setNewUrls] = useState([])
    const [errors, setErrors] = useState({})

    useEffect(() => {
        dispatch(fetchOneMemory(memoryId))
    }, [dispatch, memoryId])

    useEffect(() => {
        if (memory) {
            setTitle(memory.title)
            setDetails(memory.details)
            const urls = memory.images ? memory.images.map(image => image.url) : []
            setOgUrls(urls)
        }
    }, [dispatch, memory])

    if (!memory) {
        return <h1>Loading...</h1>
    }

    const handleOgImageChange = (i, url) => {
        const newUrls = [...ogUrls]
        newUrls[i] = url
        setOgUrls(newUrls)
    }

    const handleNewImageChange = (i, url) => {
        const newNewUrls = [...newUrls]
        newNewUrls[i] = url
        setNewUrls(newNewUrls)
    }

    const addImageField = () => {
        setNewUrls([...newUrls, ''])
    }

    const removeImageField = (i) => {
        setNewUrls(newUrls.slice(0, i).concat(newUrls.slice(i + 1)))
    }

    const validateForm = () => {
        const validationErrors = {}

        if (title.trim().length === 0) validationErrors.title = 'Give your post a title'
        if (details.trim().length === 0) validationErrors.details = 'Tell us more about your memories'

        const isValidUrl = (ogUrls) => {
            try {
                new URL(ogUrls);
                return true;
            } catch {
                return false;
            }
        }
        if (ogUrls.some(url => !url.trim() || !isValidUrl(url.trim()))) validationErrors.ogUrls = 'Add a photo of your memory'
        const isValidNewUrl = (newUrls) => {
            try {
                new URL(newUrls);
                return true;
            } catch {
                return false;
            }
        }
        if (newUrls.some(url => !url.trim() || !isValidNewUrl(url.trim()))) validationErrors.newUrls = 'Add a photo of your item'
        return validationErrors
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const validationErrors = validateForm()

        if (Object.values(validationErrors).length > 0) {
            setErrors(validationErrors)
            return;
        } else {
            const payload = {
                title: title.trim(),
                details: details.trim()
            }
            const updatedMem = await dispatch(fetchEditMemory(payload, memoryId))

        if (updatedMem) {
            for (let i = 0; i < ogUrls.length; i++) {
                await dispatch(fetchEditImage({
                    url: ogUrls[i].trim(),
                    memory_id: memoryId,
                    image_id: memory.images[i].id
                }))
            }

            for (let url of newUrls) {
                await dispatch(fetchAddImage({
                    url: url.trim(),
                    memory_id: memoryId
                }))
            }


                navigate(`/memories/${memoryId}`)
            }
        }
    }

    return (
        <>
        <h1 className="create-memory-header">Update Your Memory</h1>
        <form className="create-memory-form" onSubmit={handleSubmit}>
            <label className="create-memory-form-title">
                Title
                <input
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Title"
                />
            </label>
            {errors.title && <p className="form-errors">{errors.title}</p>}
            <label className="create-memory-form-details">
                Details
                <textarea
                    value={details}
                    onChange={(e) => setDetails(e.target.value)}
                    placeholder="Details"
                    rows='5'
                />
            </label>
            {errors.details && <p className="form-errors">{errors.details}</p>}
            <div className="input-image">
                    {ogUrls.length <= 1 ? 'Original Image' : 'Original Images'}
            </div>
            {ogUrls.map((url, i) => (
                    <Fragment key={i}>
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleOgImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                        {errors.ogUrls && <p className="form-errors">{errors.ogUrls}</p>}
                    </Fragment>
                ))}
                <div className="input-image-update">
                    Add a New Image
                </div>
                {newUrls.map((url, i) => (
                    <Fragment key={i}>
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleNewImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                <span className="remove-image-button-span">
                        <button className="remove-image-field" type="button" onClick={() => removeImageField(i)}>Remove</button>
                    </span>
                        {errors.newUrls && <p className="form-errors">{errors.newUrls}</p>}
                    </Fragment>
                ))}
                <button className="add-another-image" type='button' onClick={addImageField}>Add Another Image</button>
                <button className="memory-form-submit" type="submit">Update Memory</button>
            </form>
        </>
    )
}

export default UpdateMemory
