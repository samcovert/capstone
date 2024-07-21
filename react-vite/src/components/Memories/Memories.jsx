import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAddLike, fetchAllMemories, fetchDeleteLike } from "../../redux/memories"
import { NavLink, useNavigate } from "react-router-dom"
import './Memories.css'
import { BiSolidLike } from "react-icons/bi"
import OpenModalButton from "../OpenModalButton/OpenModalButton"
import LoginFormModal from "../LoginFormModal"


const Memories = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const memories = useSelector(state => Object.values(state.memories))
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(fetchAllMemories())
    }, [dispatch])

    const [currentIndexes, setCurrentIndexes] = useState({});

    useEffect(() => {
        if (memories.length > 0 && Object.keys(currentIndexes).length === 0) {
            const initialIndexes = {};
            memories.forEach(mem => {
                initialIndexes[mem.id] = 0;
            });
            setCurrentIndexes(initialIndexes)
        }
    }, [memories, currentIndexes])

    const handlePrev = (id, length) => {
        setCurrentIndexes(prev => ({
            ...prev,
            [id]: (prev[id] - 1 + length) % length
        }));
    };

    const handleNext = (id, length) => {
        setCurrentIndexes(prev => ({
            ...prev,
            [id]: (prev[id] + 1) % length
        }));
    };

    const handleLike = (mem, e) => {
        e.preventDefault()
        if (user) {
            const userLike = mem.user_likes.find(like => like.user_id === user.id)
            if (userLike) {
                dispatch(fetchDeleteLike(userLike.id, mem.id))
            } else {
                dispatch(fetchAddLike(mem.id))
            }
        } else {
            alert('Sign in to like this post.')
        }
    }

    if (!memories) {
        return <h1>Loading...</h1>
    }

    return (
        <>
            <div className="mem-container">
                <h1 className="mem-title">Coyotes Memories</h1>
                <div className="mem-description">
                    <p className="mem-sub">
                        Feeling nostalgic for Coyotes hockey? Well you&apos;ve come to the right place!
                    </p>
                    {!user ? (
                        <OpenModalButton
                            buttonText='Sign in to join the fun'
                            modalComponent={<LoginFormModal />}
                        />
                    ) : <div className="new-post-div"><button className="new-post-button" onClick={() => navigate('/memories/new')}>Make a new memory</button> </div>}
                </div>
                {memories?.map(mem => (
                    <NavLink key={mem.id} to={`/memories/${mem.id}`}>
                        <div className="mem-card">
                            <div className="mem-card-user">{mem.user?.username}</div>
                            <div className="mem-carousel">
                                {mem.images?.map((image, index) => (
                                    <div
                                        key={index}
                                        className={`mem-carousel-item ${currentIndexes[mem.id] === index ? 'active' : ''}`}
                                    >
                                        <img className="mem-image" src={image.url} alt={mem.name} />
                                    </div>
                                ))}
                                {mem.images?.length > 1 &&
                                    <>
                                        <button className="mem-carousel-arrow left" onClick={(e) => { e.preventDefault(); handlePrev(mem.id, mem.images.length) }}>{'<'}</button>
                                        <button className="mem-carousel-arrow right" onClick={(e) => { e.preventDefault(); handleNext(mem.id, mem.images.length) }}>{'>'}</button>
                                    </>
                                }
                            </div>
                            <div className="mem-bottom">
                                <div className="mem-name">
                                    {mem.title}
                                </div>
                                <div className="mem-bottom-actions">
                                    <button
                                        className={`like-button ${mem.user_likes?.some(like => like.user_id === user.id) ? 'liked' : ''}`}
                                        onClick={(e) => handleLike(mem, e)}><BiSolidLike /> {mem.likes}
                                    </button>
                                    <div className="mem-bottom-comments">
                                        {mem.comments?.length} {mem.comments?.length === 1 ? 'comment' : 'comments'}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </NavLink>
                ))}
            </div>
        </>
    )
}

export default Memories
