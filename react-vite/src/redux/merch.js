const GET_ALL_MERCH = '/merch/GET_ALL_MERCH'
const GET_ONE_MERCH = '/merch/GET_ONE_MERCH'
const CREATE_MERCH = '/merch/CREATE_MERCH'
const ADD_IMAGE = '/merch/ADD_IMAGE'

const getAllMerch = merch => {
    return {
        type: GET_ALL_MERCH,
        merch
    }
}

const getOneMerch = merch => {
    return {
        type: GET_ONE_MERCH,
        merch
    }
}

const createMerch = merch => {
    return {
        type: CREATE_MERCH,
        merch
    }
}

const addImage = image => {
    return {
        type: ADD_IMAGE,
        image
    }
}

export const fetchAllMerch = () => async (dispatch) => {
    const res = await fetch('/api/merch/')

    if (res.ok) {
        const merch = await res.json()
        dispatch(getAllMerch(merch))
        return merch
    }
}

export const fetchMerchDetails = (merchId) => async (dispatch) => {
    const res = await fetch(`/api/merch/${merchId}/`)

    if (res.ok) {
        const merch = await res.json()
        dispatch(getOneMerch(merch))
        return merch
    }
}

export const fetchCreateMerch = (merch) => async (dispatch) => {
    const res = await fetch('/api/merch/new/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(merch)
    })

    if (res.ok) {
        const newMerch = await res.json()
        dispatch(createMerch(newMerch))
        return newMerch
    }
}

export const fetchAddImage = (image) => async (dispatch) => {
    const res = await fetch('/api/merch/new/image/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(image)
    })
    if (res.ok) {
        const newImage = await res.json()
        dispatch(addImage(newImage))
        return newImage
    }
}
const initialState = {}
const merchReducer = (state=initialState, action) => {
    switch (action.type) {
        case GET_ALL_MERCH: {
            const merchState = { ...state }
            action.merch.forEach(merchandise => (merchState[merchandise.id] = merchandise))
            return merchState
        }
        case GET_ONE_MERCH: {
            return {
                ...state,
                [action.merch.id]: action.merch
            }
        }
        case CREATE_MERCH: {
            const newState = {
                ...state,
                [action.merch.id]: action.merch
            }
            return newState
        }
        case ADD_IMAGE: {
            const newState = {
                ...state,
                [action.image.id]: action.image
            }
            return newState
        }
        default:
            return state;
    }
}

export default merchReducer;
