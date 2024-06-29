import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { fetchAllMerch } from "../../redux/merch"
import { NavLink } from "react-router-dom"
import OpenModalButton from "../OpenModalButton"
import DeleteMerch from "../DeleteMerch"

const UserProfile = () => {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const merch = useSelector(state => Object.values(state.merchandise).filter(item => item.user_id === user.id))

    useEffect(() => {
        dispatch(fetchAllMerch())
    }, [dispatch])

    return (
        <>
        <h1>Your Items for Sale</h1>
            {merch.map(item => (
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
        </>
    )
}

export default UserProfile
