import { Fragment, useState } from "react"
import { useDispatch } from "react-redux"
import { useNavigate } from "react-router-dom"
import { fetchCreateMemory, fetchAddImage } from "../../redux/memories"
import './CreateMemory.css'

const CreateMemory = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const [title, setTitle] = useState('')
    const [details, setDetails] = useState('')
    const [urls, setUrls] = useState([''])
    const [errors, setErrors] = useState({})

    const handleImageChange = (i, url) => {
        const newUrls = [...urls]
        newUrls[i] = url
        setUrls(newUrls)
    }

    const addImageField = () => {
        setUrls([...urls, ''])
    }

    const removeImageField = (i) => {
        setUrls(urls.slice(0, i).concat(urls.slice(i + 1)))
    }

    const validateForm = () => {
        const validationErrors = {}

        if (title.trim().length === 0) validationErrors.title = 'Give your post a title'
        if (details.trim().length === 0) validationErrors.details = 'Tell us more about your memories'

        const isValidUrl = (url) => {
            try {
                new URL(url);
                return true;
            } catch {
                return false;
            }
        }
        if (urls.some(url => !url.trim() || !isValidUrl(url.trim()))) validationErrors.urls = 'Add a photo of your memory'

        return validationErrors
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const validationErrors = validateForm()

        if (Object.values(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        } else {
            const payload = {
                title: title.trim(),
                details: details.trim()
            }
            const newMem = await dispatch(fetchCreateMemory(payload))

            if (newMem) {
                const newMemId = newMem.id;

                for (let url of urls) {
                    await dispatch(fetchAddImage({
                        url: url.trim(),
                        memory_id: +newMemId
                    }));
                }
                navigate(`/memories/${+newMem.id}`);
            }
        }
    }

    return (
        <>
        <h1 className="create-memory-header">Create a Memory</h1>
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
                Add an Image
            </div>
            {urls.map((url, i) => (
                    <Fragment key={i}>
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                        {i !== 0 && (
                       <span className="remove-image-button-span">
                       <button className="remove-image-field" type="button" onClick={() => removeImageField(i)}>Remove</button>
                       </span>
                        )}
                        {errors.urls && <p className="form-errors">{errors.urls}</p>}
                    </Fragment>
                ))}
                <button className="add-another-image" type='button' onClick={addImageField}>Add Another Image</button>
                <button className="memory-form-submit" type="submit">Post Memory</button>
        </form>
        </>
    )
}

export default CreateMemory
