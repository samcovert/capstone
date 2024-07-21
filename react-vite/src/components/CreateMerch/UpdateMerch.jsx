import { Fragment, useEffect, useState } from "react"
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
    const [price, setPrice] = useState('');
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
            setPrice(merch.price || '');
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

        if (name.trim().length === 0) validationErrors.name = 'Give your item a name'
        if (description.trim().length === 0) validationErrors.description = 'Give your item a description'
        if (!price || isNaN(price) || parseFloat(price) <= 0) validationErrors.price = 'Your Product needs a price'
        const isValidUrl = (ogUrls) => {
            try {
                new URL(ogUrls);
                return true;
            } catch {
                return false;
            }
        }
        if (ogUrls.some(url => !url.trim() || !isValidUrl(url.trim()))) validationErrors.ogUrls = 'Add a photo of your item'
        const isValidNewUrl = (newUrls) => {
            try {
                new URL(newUrls);
                return true;
            } catch {
                return false;
            }
        }
        if (newUrls.some(url => !url.trim() || !isValidNewUrl(url.trim()))) validationErrors.newUrls = 'Add a photo of your item'
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
                name: name.trim(),
                description: description.trim(),
                price: price
            }
            const updatedItem = await dispatch(fetchEditItem(payload, merchId))

            for (let i = 0; i < ogUrls.length; i++) {
                await dispatch(fetchEditImage({
                    url: ogUrls[i].trim(),
                    merch_id: merchId,
                    image_id: merch.images[i].id
                }))
            }

            for (let url of newUrls) {
                await dispatch(fetchAddImage({
                    url: url.trim(),
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
                <div className="input-image">
                    {ogUrls.length <= 1 ? 'Original Image' : 'Original Images'}
                </div>
                {ogUrls.map((url, i) => (
                    <Fragment key={i}>
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleOgImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                        {errors.ogUrls && <p className="form-errors">{errors.ogUrls}</p>}
                    </Fragment>
                ))}
                <div className="input-image-update">
                    Add a New Image
                    </div>
                {newUrls.map((url, i) => (
                    <Fragment key={i}>

                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleNewImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                <span className="remove-image-button-span">
                        <button className="remove-image-field" type="button" onClick={() => removeImageField(i)}>Remove</button>
                    </span>
                        {errors.newUrls && <p className="form-errors">{errors.newUrls}</p>}
                    </Fragment>
                ))}
                <button className="add-another-image" type='button' onClick={addImageField}>Add Another Image</button>
                <button className="merch-form-submit" type="submit">Update Item</button>
            </form>
        </>
    )
}

export default UpdateMerch
