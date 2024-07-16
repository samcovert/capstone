import { useState } from "react"
import { useDispatch } from "react-redux"
import { useNavigate } from "react-router-dom"
import { fetchCreateMemory, fetchAddImage } from "../../redux/memories"


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
                title: title,
                details: details
            }
            const newMem = await dispatch(fetchCreateMemory(payload))
            const newMemId = newMem.id

            for (let url of urls) {
                await dispatch(fetchAddImage({
                    url: url,
                    merch_id: +newMemId
                }))
            }
            if (newMem) {
                navigate(`/memories/${+newMem.id}`)
            }
        }
    }
    return (
        <>
        <h1>Create a Memory</h1>
        <form className="create-memory-form" onSubmit={handleSubmit}>
            <label>
                Title
                <input
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Title"
                />
            </label>
            {errors.title && <p className="form-errors">{errors.title}</p>}
            <label>
                Details
                <input
                    type="text"
                    value={details}
                    onChange={(e) => setDetails(e.target.value)}
                    placeholder="Details"
                />
            </label>
            {errors.details && <p className="form-errors">{errors.details}</p>}
            {urls.map((url, i) => (
                    <div key={i}>
                        <label className="input-image">
                            Add an Image
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                        </label>
                        {i !== 0 && (
                        <button type="button" onClick={() => removeImageField(i)}>Remove</button>
                        )}
                        {errors.urls && <p className="form-errors">{errors.urls}</p>}
                    </div>
                ))}
                <button type='button' onClick={addImageField}>Add Another Image</button>
                <button className="Memory-form-submit" type="submit">Post Memory</button>
        </form>
        </>
    )
}

export default CreateMemory
