import { useDispatch, useSelector } from 'react-redux'
import './Merchandise.css'
import { useEffect } from 'react'
import { fetchAllMerch } from '../../redux/merch'
import { Link } from 'react-router-dom'

const Merchandise = () => {
    const dispatch = useDispatch()
    const merchandise = useSelector(state => Object.values(state.merchandise))

    useEffect(() => {
        dispatch(fetchAllMerch())
    }, [dispatch])

    return (
        <>
        <h1>Merch</h1>
        {merchandise.map(merch => (
            <Link to={`/merch/${merch.id}`} key={merch.id}>
                <img src={merch.images[0].url}></img>
                {merch.name}
                {merch.price}
            </Link>
        ))}
        </>
    )
}

export default Merchandise
