const GET_ALL_MERCH = '/merch/GET_ALL_MERCH'
const GET_ONE_MERCH = '/merch/GET_ONE_MERCH'

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
        default:
            return state;
    }
}

export default merchReducer;
