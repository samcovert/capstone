import { Fragment, useState } from "react"
import { useDispatch } from "react-redux"
import { fetchAddImage, fetchCreateMerch } from "../../redux/merch"
import { useNavigate } from "react-router-dom"
import './CreateMerch.css'


const CreateMerch = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const [name, setName] = useState('')
    const [description, setDescription] = useState('')
    const [price, setPrice] = useState('')
    const [urls, setUrls] = useState([''])
    const [errors, setErrors] = useState({})

    const handleImageChange = (i, url) => {
        const newUrls = [...urls]
        newUrls[i] = url
        setUrls(newUrls)
    }

    const addImageField = () => {
        setUrls([...urls, ''])
    }

    const removeImageField = (i) => {
        setUrls(urls.slice(0, i).concat(urls.slice(i + 1)))
    }

    const validateForm = () => {
        const validationErrors = {}

        if (name.trim().length === 0) validationErrors.name = 'Give your item a name'
        if (description.trim().length === 0) validationErrors.description = 'Give your item a description'
        if (price.trim().length === 0 || isNaN(price) || parseFloat(price) <= 0) validationErrors.price = 'Your Product needs a price'

        const isValidUrl = (url) => {
            try {
                new URL(url);
                return true;
            } catch {
                return false;
            }
        }
        if (urls.some(url => !url.trim() || !isValidUrl(url.trim()))) validationErrors.urls = 'Add a photo of your item'

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
                price: price.trim()
            }
            const newItem = await dispatch(fetchCreateMerch(payload))
            const newItemId = newItem.id

            for (let url of urls) {
                await dispatch(fetchAddImage({
                    url: url.trim(),
                    merch_id: +newItemId
                }))
            }

            if (newItem) {
                navigate(`/merch/${+newItem.id}`)
            }
        }
    }

    return (
        <>
            <h1 className="create-merch-header">Create a New Item To Sell!</h1>
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
                    Add an Image
                </div>
                {urls.map((url, i) => (
                    <Fragment key={i}>
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                        {i !== 0 && (
                       <span className="remove-image-button-span">
                       <button className="remove-image-field" type="button" onClick={() => removeImageField(i)}>Remove</button>
                       </span>
                        )}
                        {errors.urls && <p className="form-errors">{errors.urls}</p>}
                    </Fragment>
                ))}
                <button className="add-another-image" type='button' onClick={addImageField}>Add Another Image</button>
                <button className="merch-form-submit" type="submit">Create Item</button>
            </form>
        </>
    )
}

export default CreateMerch
