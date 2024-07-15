import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from "react-router-dom"
import { fetchEditNews, fetchNewsDetails } from "../../redux/news"


const UpdateNews = () => {
    let { newsId } = useParams()
    newsId = +newsId
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const news = useSelector(state => state.news[newsId])
    const [title, setTitle] = useState('')
    const [details, setDetails] = useState('')
    const [errors, setErrors] = useState({})

    useEffect(() => {
        dispatch(fetchNewsDetails(newsId))
    }, [dispatch, newsId])

    useEffect(() => {
        if (news) {
            setTitle(news.title);
            setDetails(news.details);
        }
    }, [dispatch, news])

    if (!news) {
        return <h1>Loading...</h1>
    }

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
            const updatedNews = await dispatch(fetchEditNews(payload, newsId))

            if (updatedNews) navigate(`/news/${newsId}`)
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

export default UpdateNews;
