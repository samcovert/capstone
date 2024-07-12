import { useState } from "react"
import { useDispatch } from "react-redux"
import { fetchAddImage, fetchCreateMerch } from "../../redux/merch"
import { useNavigate } from "react-router-dom"


const CreateMerch = () => {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const [name, setName] = useState('')
    const [description, setDescription] = useState('')
    const [price, setPrice] = useState(0)
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
                name: name,
                description: description,
                price: price
            }
            const newItem = await dispatch(fetchCreateMerch(payload))
            const newItemId = newItem.id

            for (let url of urls) {
                await dispatch(fetchAddImage({
                    url: url,
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
                {urls.map((url, i) => (
                    <div key={i}>
                        <label className="input-image">
                            Add an Image
                            <input
                                type="text"
                                value={url}
                                onChange={(e) => handleImageChange(i, e.target.value)}
                                placeholder="Image URL"
                            />
                        </label>
                        {i !== 0 && (
                        <button type="button" onClick={() => removeImageField(i)}>Remove</button>
                        )}
                        {errors.urls && <p className="form-errors">{errors.urls}</p>}
                    </div>
                ))}
                <button type='button' onClick={addImageField}>Add Another Image</button>
                <button className="merch-form-submit" type="submit">Create Item</button>
            </form>
        </>
    )
}

export default CreateMerch
