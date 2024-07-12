import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAllMemories } from "../../redux/memories"
import { NavLink } from "react-router-dom"


const Memories = () => {
    const dispatch = useDispatch()
    const memories = useSelector(state => Object.values(state.memories))

    useEffect(() => {
        dispatch(fetchAllMemories())
    }, [dispatch])

    return (
        <>
        <h1>Memories</h1>
        {memories.map(mem => (
            <NavLink to={`/memories/${mem.id}`}>
                <div key={mem.id}>
                    <img src={mem.images[0].url}></img>
                    <div>{mem.user.username}</div>
                    <div>{mem.title}</div>
                    <div>{mem.details}</div>
                    <div>{mem.likes}</div>
                    <div>{mem.comments.length} comments</div>
                </div>
            </NavLink>
        ))}
        </>
    )
}

export default Memories
