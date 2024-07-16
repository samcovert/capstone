import { useState } from "react"
import { useDispatch } from "react-redux"
import { useNavigate } from "react-router-dom"
import { fetchCreateNews } from "../../redux/news"


const CreateNews = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const [title, setTitle] = useState('')
    const [details, setDetails] = useState('')
    const [errors, setErrors] = useState({})

    const handleSubmit = async (e) => {
        e.preventDefault()
        const validationErrors = {}

        if (title.length === 0) validationErrors.title = 'Give your post a title'
        if (details.length === 0) validationErrors.details = 'Your post needs some content'
        if (Object.values(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        } else {
            const payload = {
                title: title,
                details: details
            }
            const newNews = await dispatch(fetchCreateNews(payload))

            if (newNews) navigate(`/news/${+newNews.id}`)
        }
    }

    return (
        <>
            <h1>Start a discussion about some Coyotes news!</h1>
            <form onSubmit={handleSubmit}>
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
                    {errors.details && <p className="form-errors">{errors.details}</p>}
                    <button type="submit">Post</button>
                </label>
            </form>
        </>
    )
}

export default CreateNews
