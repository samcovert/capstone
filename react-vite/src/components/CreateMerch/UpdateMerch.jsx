import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from "react-router-dom"
import { fetchAddImage, fetchEditImage, fetchEditItem, fetchMerchDetails } from "../../redux/merch"

const UpdateMerch = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    let { merchId } = useParams()
    merchId = +merchId
    const merch = useSelector(state => state.merchandise[+merchId])
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [price, setPrice] = useState(0);
    const [ogUrls, setOgUrls] = useState([])
    const [newUrls, setNewUrls] = useState([])
    const [errors, setErrors] = useState({})
    useEffect(() => {
        dispatch(fetchMerchDetails(merchId));
    }, [dispatch, merchId]);

    useEffect(() => {
        if (merch) {
            setName(merch.name || '');
            setDescription(merch.description || '');
            setPrice(merch.price || 0);
            const urls = merch.images ? merch.images.map(image => image.url) : []
            setOgUrls(urls)
        }
    }, [dispatch, merch])

    if (!merch) {
        return <h1>Loading...</h1>
    }

    const handleOgImageChange = (i, url) => {
        const newUrls = [...ogUrls]
        newUrls[i] = url
        setOgUrls(newUrls)
    }

    const handleNewImageChange = (i, url) => {
        const newNewUrls = [...newUrls]
        newNewUrls[i] = url
        setNewUrls(newNewUrls)
    }

    const addImageField = () => {
        setNewUrls([...newUrls, ''])
    }

    const removeImageField = (i) => {
        setNewUrls(newUrls.slice(0, i).concat(newUrls.slice(i + 1)))
    }

    const validateForm = () => {
        const validationErrors = {}

        if (name.length === 0) validationErrors.name = 'Give your item a name'
        if (description.length === 0) validationErrors.description = 'Give your item a description'
        if (price === 0) validationErrors.price = 'Your Product needs a price'
        if (ogUrls.some(url => !url)) validationErrors.ogUrls = 'Add a photo of your item'

        return validationErrors
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const validationErrors = validateForm()

        if (Object.values(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        } else {
            const payload = {
                name: name,
                description: description,
                price: price
            }
            const updatedItem = await dispatch(fetchEditItem(payload, merchId))

            for (let i = 0; i < ogUrls.length; i++) {
                await dispatch(fetchEditImage({
                    url: ogUrls[i],
                    merch_id: merchId,
                    image_id: merch.images[i].id
                }))
            }

            for (let url of newUrls) {
                await dispatch(fetchAddImage({
                    url: url,
                    merch_id: merchId
                }));
            }


            if (updatedItem) {
                navigate(`/merch/${merchId}`)
            }
        }
    }

    return (
        <>
            <h1 className="create-merch-header">Update Your Item</h1>
            <form className="create-merch-form" onSubmit={handleSubmit}>
                <label className="input-name">
                    Item Name
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        placeholder="Item Name"
                    />
                </label>
                {errors.name && <p className="form-errors">{errors.name}</p>}
                <label className="input-description">
                    Description
                    <input
                        type="text"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        placeholder="Description"
                    />
                </label>
                {errors.description && <p className="form-errors">{errors.description}</p>}
                <label className="input-price">
                    Price
                    <input
                        type="text"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                        placeholder="$0.00"
                    />
                </label>
                {errors.price && <p className="form-errors">{errors.price}</p>}
                {ogUrls.map((url, i) => (
                    <div key={i}>
                        <label className="input-image">
                            Original Image
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleOgImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                        </label>
                        {errors.urls && <p className="form-errors">{errors.urls}</p>}
                    </div>
                ))}
                {newUrls.map((url, i) => (
                    <div key={i}>
                        <label className="input-image">
                            Add a New Image
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleNewImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                        </label>
                        <button type="button" onClick={() => removeImageField(i)}>Remove</button>
                    </div>
                ))}
                <button type='button' onClick={addImageField}>Add Another Image</button>
                <button className="merch-form-submit" type="submit">Update Item</button>
            </form>
        </>
    )
}

export default UpdateMerch
