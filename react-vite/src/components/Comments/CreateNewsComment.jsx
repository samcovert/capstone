import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAddComment, fetchEditComment, fetchNewsDetails } from "../../redux/news"
import { useModal } from "../../context/Modal"
import './CreateComment.css'


const CreateNewsComment = ({ newsId, comment=null }) => {
    const dispatch = useDispatch()
    const [content, setContent] = useState(comment ? comment.content : '')
    const [errors, setErrors] = useState({})
    const user = useSelector(state => state.session.user)
    const { closeModal } = useModal()

    useEffect(() => {
        if (comment) {
            setContent(comment.content)
        }
    }, [comment])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const validationErrors = {}

        if (content.trim().length === 0) validationErrors.content = 'Your review needs some text'

        if (Object.values(validationErrors).length > 0) {
            setErrors(validationErrors)
            return
        } else {
            const payload = {
                content: content.trim(),
                user_id: user.id,
                news_id: newsId
            }
            if (comment) {
                const updatedComment = await dispatch(fetchEditComment(payload, comment.id, newsId))
                if (updatedComment) {
                    dispatch(fetchNewsDetails(newsId))
                    closeModal()
                }
            } else {
                const newComment = await dispatch(fetchAddComment(payload))
                if (newComment) {
                    closeModal()
                    dispatch(fetchNewsDetails(newsId))
                }
            }
        }
    }

    return (
        <>
        <div className="comment-modal-container">
            <h1 className="comment-header">Join the Discussion</h1>
            <form className="comment-form" onSubmit={handleSubmit}>
                <textarea
                    type="text"
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    placeholder="Leave Your Thoughts"
                />
                {errors.content && <p className="form-errors">{errors.content}</p>}
                <button className="comment-submit" type="submit">{comment ? 'Update Comment' : 'Post Comment'}</button>
            </form>
            </div>
        </>
    )
}

export default CreateNewsComment
