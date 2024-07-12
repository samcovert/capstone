import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { fetchOneMemory } from "../../redux/memories"


const MemoryDetails = () => {
    let { memoryId } = useParams()
    memoryId = +memoryId
    const dispatch = useDispatch()
    const memory = useSelector(state => state.memories[memoryId])

    useEffect(() => {
        dispatch(fetchOneMemory(memoryId))
    }, [dispatch])

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
        <div>
            {memory.comments.map(comment => (
                <div key={comment.id}>
                    {comment.content}
                    {comment.users.username}
                </div>
            ))}
        </div>
        </>
    )
}

export default MemoryDetails
