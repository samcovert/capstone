const GET_ALL_MEMORIES = '/memories/GET_ALL_MEMORIES'
const GET_ONE_MEM = '/memories/GET_ONE_MEM'

const getAllMemories = memories => {
    return {
        type: GET_ALL_MEMORIES,
        memories
    }
}

const getOneMemory = memory => {
    return {
        type: GET_ONE_MEM,
        memory
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

export const fetchOneMemory = (memId) => async (dispatch) => {
    const res = await fetch(`/api/memories/${memId}`)

    if (res.ok) {
        const mem = await res.json()
        dispatch(getOneMemory(mem))
        return mem
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
        case GET_ONE_MEM: {
            return {
                ...state,
                [action.memory.id]: action.memory
            }
        }
        default:
            return state
    }
}

export default memsReducer
