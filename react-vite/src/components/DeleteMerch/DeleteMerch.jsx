import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useState } from "react";
import { fetchDeleteMerch } from "../../redux/merch";
import './Delete.css'


const DeleteMerch = ({ merchId }) => {
    const { closeModal } = useModal()
    const dispatch = useDispatch()
    const [errors, setErrors] = useState({})

    const handleClick = (e) => {
        e.preventDefault()
        setErrors({})
        dispatch(fetchDeleteMerch(merchId))
            .then(closeModal)
            .catch(async (res) => {
                let data = await res.json()
                if (data && data.errors) setErrors(data.errors)
            })
    }

    return (
        <>
        <div className="delete-modal-container">
        <h1 className="delete-form-header">Are you sure you want to delete this item?</h1>
                <form className="delete-form">
                    {errors.message && (
                        <div className="form-errors">{errors.message}</div>
                    )}
                    <div className="delete-actions">
                        <button className="delete-button" onClick={handleClick}>Yes</button>
                        <button className="cancel-button" onClick={closeModal}>No</button>
                    </div>
                </form>
        </div>
        </>
    )
}

export default DeleteMerch;
