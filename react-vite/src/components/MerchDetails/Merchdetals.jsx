import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { fetchMerchDetails } from "../../redux/merch"


const MerchDetails = () => {
    let { merchId } = useParams()
    merchId = +merchId
    const dispatch = useDispatch()
    const merch = useSelector(state => state.merchandise[+merchId])

    useEffect(() => {
            dispatch(fetchMerchDetails(merchId))
    }, [dispatch, merchId])
    if (!merch) {
        return (
            <h1>Loading...</h1>
        )
    }

    return (
        <>
        {merch.images.map(image => (
            <img key={image.id} src={image.url}></img>
        ))}
        <h1>{merch.name}</h1>
        {merch.desctiption}
        {merch.price}
        </>
    )
}

export default MerchDetails
