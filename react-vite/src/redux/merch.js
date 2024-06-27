const GET_ALL_MERCH = '/merch/GET_ALL_MERCH'

const getMerch = (merch) => {
    return {
        type: GET_ALL_MERCH,
        merch
    }
}

export const fetchAllMerch = () => async (dispatch) => {
    const res = await fetch('/api/merch/')

    if (res.ok) {
        const merch = await res.json()
        dispatch(getMerch(merch))
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
        default:
            return state;
    }
}

export default merchReducer;
