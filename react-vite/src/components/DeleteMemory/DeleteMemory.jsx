import { useDispatch } from "react-redux"
import { useModal } from "../../context/Modal"
import { useState } from "react"
import { fetchDeleteMemory } from "../../redux/memories"


const DeleteMemory = ({ memoryId }) => {
    const { closeModal } = useModal()
    const dispatch = useDispatch()
    const [errors, setErrors] = useState({})

    const handleClick = (e) => {
        e.preventDefault()
        setErrors({})
        dispatch(fetchDeleteMemory(memoryId))
            .then(closeModal)
            .catch(async (res) => {
                let data = await res.json()
                if (data && data.errors) setErrors(data.errors)
            })
    }
    return (
        <>
        <div className="delete-modal">
            <div className="delete-content">
            <form>
                <h3>Are you sure you want to delete this memory?</h3>
                    {errors.message && (
                        <div className="errors">{errors.message}</div>
                    )}
                    <div className="delete-actions">
                        <button className="delete-button" onClick={handleClick}>Yes (Delete It)</button>
                        <button className="cancel-button" onClick={closeModal}>No (Keep It)</button>
                    </div>
                </form>
            </div>
        </div>
        </>
    )
}

export default DeleteMemory
