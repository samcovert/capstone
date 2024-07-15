import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { fetchDeleteComment, fetchOneMemory } from "../../redux/memories"
import CreateMemoryComment from "../Comments/CreateMemoryComment"
import OpenModalButton from "../OpenModalButton"


const MemoryDetails = () => {
    let { memoryId } = useParams()
    memoryId = +memoryId
    const dispatch = useDispatch()
    const memory = useSelector(state => state.memories[memoryId])
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(fetchOneMemory(memoryId))
    }, [dispatch, memoryId])

    const handleDelete = async (id) => {
        await dispatch(fetchDeleteComment(id, memoryId))
    }

    if (!memory) {
        return <h1>Loading...</h1>
    }
    return (
        <>
        <h1>{memory.title}</h1>
        <div>
            {memory.images.map(img => (
                <img key={img.id} src={img.url}></img>
            ))}
        </div>
        <div>{memory.user.username}</div>
        <div>{memory.details}</div>
        <div>{memory.likes}</div>
        <div className="comments">
            <div>
                <OpenModalButton
                    modalComponent={<CreateMemoryComment memoryId={memoryId} />}
                    buttonText='Add Comment'
                />
            </div>
            {memory.comments?.length ? (
                memory.comments.map(comment => (
                <div key={comment.id}>
                    {comment.content}
                    {comment.users.username}
                    {user && user.id === comment.user_id && (
                        <div className="review-buttons">
                        <OpenModalButton
                            modalComponent={<CreateMemoryComment comment={comment} memoryId={comment.memory_id} />}
                            buttonText='Update'
                        />
                        <button onClick={() => handleDelete(comment.id)}>Delete</button>
                        </div>
                    )}
                </div>
            ))
        ): <p>No comments yet</p>
        }
        </div>
        </>
    )
}

export default MemoryDetails
