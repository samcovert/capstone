import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from "react-router-dom"
import { fetchAllMerch, fetchMerchDetails } from "../../redux/merch"
import './Merchdetails.css'


const MerchDetails = () => {
    let { merchId } = useParams()
    merchId = +merchId
    const dispatch = useDispatch()
    const merch = useSelector(state => state.merchandise[+merchId])
    const user = useSelector(state => state.session.user)
    const navigate = useNavigate()
    const [selectedImage, setSelectedImage] = useState(null)

    useEffect(() => {
        dispatch(fetchMerchDetails(merchId))
    }, [dispatch, merchId])

    useEffect(() => {
        if (merch && merch.images.length > 0) {
            setSelectedImage(merch.images[0].url)
        }
    }, [merch])

    const handleClick = () => {
        return (alert("Feature comming soom"))
    }

    const handleBack = () => {
        (dispatch(fetchAllMerch()))
            .then(navigate('/merch'))
    }

    if (!merch) {
        return (
            <h1>Loading...</h1>
        )
    }

    return (
        <>
            <div className="merch-det-page">
                <div onClick={handleBack} className="back-button">Back to store</div>
                <div className="merch-details-container">
                <h1 className="merch-det-title">{merch.name}</h1>
                    <div className="merch-det-main">
                    <div className="merch-det-left">
                    <div className="merch-det-img-section">
                        {selectedImage && <img className="merch-det-img" src={selectedImage} alt="Merchandise" />}
                        <div className="merch-det-img-thumbnails">
                            {merch.images.map(image => (
                                <img
                                    key={image.id}
                                    src={image.url}
                                    className={`thumbnail ${image.url === selectedImage ? 'active' : ''}`}
                                    onClick={() => setSelectedImage(image.url)}
                                />
                            ))}
                        </div>
                    </div>
                    </div>
                    <div className="merch-det-content">
                        <div className="sold-by">Seller: {merch.user.username}</div>
                        <div className="merch-det-description">{merch.description}</div>
                        <div className="merch-det-price">${merch.price}</div>
                        <div className="buy-now">
                            {user && (
                                <button onClick={handleClick} className="buy-now-button">Buy this item</button>
                            )}
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default MerchDetails
