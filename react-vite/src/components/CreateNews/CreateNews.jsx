import { useState } from "react"
import { useDispatch } from "react-redux"
import { useNavigate } from "react-router-dom"
import { fetchCreateNews } from "../../redux/news"
import './CreateNews.css'


const CreateNews = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const [title, setTitle] = useState('')
    const [details, setDetails] = useState('')
    const [errors, setErrors] = useState({})

    const handleSubmit = async (e) => {
        e.preventDefault()
        const validationErrors = {}

        if (title.trim().length === 0) validationErrors.title = 'Give your post a title'
        if (details.trim().length === 0) validationErrors.details = 'Your post needs some content'
        if (Object.values(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        } else {
            const payload = {
                title: title.trim(),
                details: details.trim()
            }
            const newNews = await dispatch(fetchCreateNews(payload))

            if (newNews) navigate(`/news/${+newNews.id}`)
        }
    }

    return (
        <>
            <h1 className="create-news-title">Start a discussion about some Coyotes news!</h1>
            <form className='create-news-form' onSubmit={handleSubmit}>
                <label className="create-news-input-title">
                    Title
                    <input
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder="What's your post about?"
                    />
                </label>
                {errors.title && <p className="form-errors">{errors.title}</p>}
                <label className="create-news-input-details">
                    Details
                    <textarea
                        value={details}
                        onChange={(e) => setDetails(e.target.value)}
                        placeholder="Details"
                        rows='5'
                    />
                </label>
                {errors.details && <p className="form-errors">{errors.details}</p>}
                <button className="create-news-submit" type="submit">Post</button>
            </form>
        </>
    )
}

export default CreateNews
