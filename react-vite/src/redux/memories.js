const GET_ALL_MEMORIES = '/memories/GET_ALL_MEMORIES'

const getAllMemories = memories => {
    return {
        type: GET_ALL_MEMORIES,
        memories
    }
}

export const fetchAllMemories = () => async (dispatch) => {
    const res = await fetch('/api/memories/')

    if (res.ok) {
        const mems = await res.json()
        dispatch(getAllMemories(mems))
        return mems
    }
}

const initialState = {}
const memsReducer = (state=initialState, action) => {
    switch (action.type) {
        case GET_ALL_MEMORIES: {
            const memsState = { ...state }
            action.memories.forEach(mem => (memsState[mem.id] = mem))
            return memsState
        }
        default:
            return state
    }
}

export default memsReducer
