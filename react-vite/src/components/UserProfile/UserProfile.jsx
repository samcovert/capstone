import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAllMerch } from "../../redux/merch"
import { NavLink } from "react-router-dom"
import OpenModalButton from "../OpenModalButton"
import DeleteMerch from "../DeleteMerch"
import { fetchAllNews } from "../../redux/news"
import DeleteNews from "../DeleteNews"
import { fetchAllMemories } from "../../redux/memories"
import DeleteMemory from "../DeleteMemory"

const UserProfile = () => {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const merch = useSelector(state => Object.values(state.merchandise).filter(item => item.user_id === user?.id))
    const news = useSelector(state => Object.values(state.news).filter(post => post.users?.id === user?.id))
    const memories = useSelector(state => Object.values(state.memories).filter(memory => memory.user?.id === user?.id))

    useEffect(() => {
        dispatch(fetchAllMerch())
        dispatch(fetchAllNews())
        dispatch(fetchAllMemories())
    }, [dispatch])

    return (
        <>
        <h1>Your Items for Sale</h1>
            {merch?.map(item => (
                <div key={item.id} className="user-profile-card">
                    <h2 className="user-profile-name">{item.name}</h2>
                    <NavLink to={`/merch/${item.id}`}>
                        <img className="user-profile-image" src={item.images[0]?.url} alt={item.name}></img>
                    </NavLink>
                    <NavLink to={`/merch/${item.id}/edit`}>
                        <button>Edit</button>
                    </NavLink>
                    <OpenModalButton
                        modalComponent={<DeleteMerch merchId={item.id} />}
                        buttonText='Delete'
                    />
                </div>
            ))}
        <h1>Your News Posts</h1>
            {news?.map(post => (
                <div key={post.id}>
                    <NavLink to={`/news/${post.id}`}>
                    <h3>{post.title}</h3>
                    <p>{post.details}</p>
                    </NavLink>
                    <NavLink to={`/news/${post.id}/edit`}>
                        <button>Edit</button>
                    </NavLink>
                    <OpenModalButton
                        modalComponent={<DeleteNews newsId={post.id}/>}
                        buttonText='Delete'
                    />
                </div>
            ))}
        <h1>Your Memories</h1>
            {memories?.map(memory => (
                <div key={memory.id}>
                    <NavLink to={`/memories/${memory.id}`}>
                        {memory.images?.map(img => (
                            <img key={img.id} src={img.url}></img>
                        ))}
                        <div>{memory.title}</div>
                    </NavLink>
                    <NavLink to={`/memories/${memory.id}/edit`}>
                        <button>Edit</button>
                    </NavLink>
                    <OpenModalButton
                        modalComponent={<DeleteMemory memoryId={memory.id} />}
                        buttonText='Delete'
                    />
                </div>
            ))}
        </>
    )
}

export default UserProfile
