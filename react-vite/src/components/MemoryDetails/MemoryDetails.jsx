import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from "react-router-dom"
import { fetchDeleteComment, fetchOneMemory, fetchAddLike, fetchDeleteLike, fetchAllMemories } from "../../redux/memories"
import CreateMemoryComment from "../Comments/CreateMemoryComment"
import OpenModalButton from "../OpenModalButton"
import { BiSolidLike } from "react-icons/bi"
import './MemoryDetails.css'
import LoginFormModal from "../LoginFormModal"


const MemoryDetails = () => {
    let { memoryId } = useParams()
    memoryId = +memoryId
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const memory = useSelector(state => state.memories[memoryId])
    const user = useSelector(state => state.session.user)
    const [selectedImage, setSelectedImage] = useState(null)

    useEffect(() => {
        dispatch(fetchOneMemory(memoryId))
    }, [dispatch, memoryId])

    useEffect(() => {
        if (memory && memory.images.length > 0) {
            setSelectedImage(memory.images[0].url)
        }
    }, [memory])

    const handleDelete = async (id) => {
        await dispatch(fetchDeleteComment(id, memoryId))
    }

    const handleLike = (memory, e) => {
        e.preventDefault()
        if (user) {
            const userLike = memory.user_likes.find(like => like.user_id === user.id)
            if (userLike) {
                dispatch(fetchDeleteLike(userLike.id, memory.id))
            } else {
                dispatch(fetchAddLike(memory.id))
            }
        } else {
            alert('Sign in to like this post.')
        }
    }

    const checkComments = () => {
        const comments = memory?.comments?.find(comment => comment.user_id === user.id)
        return comments
    }

    if (!memory) {
        return <h1>Loading...</h1>
    }
    return (
        <>
            <div className="back-button" onClick={async() => { await dispatch(fetchAllMemories()); navigate('/memories') }}>Back to memories</div>
            <div className="mem-det-container">
                <div className="mem-det-user">{memory.user.username}&apos;s post:</div>
                <h1 className="mem-det-title">{memory.title}</h1>
                <div className="mem-det-image-section">
                    {selectedImage && <img className="mem-det-image" src={selectedImage} />}
                    <div className="mem-det-image-thumbnails">
                        {memory.images?.map(image => (
                            <img
                                key={image.id}
                                src={image.url}
                                className={`mem-det-thumbnail ${image.url === selectedImage ? 'active' : ''}`}
                                onClick={() => setSelectedImage(image.url)}
                            />
                        ))}
                    </div>
                </div>
                <div className="mem-det-content-container">
                    <div className="mem-det-content">{memory.details}</div>
                    <button
                        className={`like-button ${memory.user_likes?.some(like => like.user_id === user?.id) ? 'liked' : ''}`}
                        onClick={(e) => handleLike(memory, e)}><BiSolidLike /> {memory.likes}
                    </button>
                </div>
            </div>
            <div className="mem-det-comments-container">
                {user ? (
                    <div className="mem-det-add-comment-button">
                        <OpenModalButton
                            modalComponent={<CreateMemoryComment memoryId={memoryId} />}
                            buttonText={!checkComments() ? 'Add Comment' : 'Add Another Comment'}
                        />
                    </div>
                ) : (
                    <div className="mem-det-add-comment-button">
                        <OpenModalButton
                            buttonText='Sign in to join the discussion'
                            modalComponent={<LoginFormModal />}
                        />
                    </div>
                )}
                {memory.comments?.length ? (
                    memory.comments.map(comment => (
                        <div className="mem-det-comments" key={comment.id}>
                            <div className="mem-det-comment-user">{comment.users.username}</div>
                            <div className="mem-det-comment-content">{comment.content}</div>
                            {user && user.id === comment.user_id && (
                                <div className="mem-det-comment-buttons">
                                        <OpenModalButton
                                            modalComponent={<CreateMemoryComment comment={comment} memoryId={comment.memory_id} />}
                                            buttonText='Edit'
                                        />
                                    <button className="mem-det-comment-delete" onClick={() => handleDelete(comment.id)}>Delete</button>
                                </div>
                            )}
                        </div>
                    ))
                ) : <p className="mem-det-no-comments">No comments yet</p>
                }
            </div>
        </>
    )
}

export default MemoryDetails
