const GET_ALL_MEMORIES = '/memories/GET_ALL_MEMORIES'
const GET_ONE_MEM = '/memories/GET_ONE_MEM'
const CREATE_MEMORY = '/memories/CREATE_MEMORY'
const ADD_IMAGE = '/memories/ADD_IMAGE'

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

const createMemory = memory => {
    return {
        type: CREATE_MEMORY,
        memory
    }
}

const addImage = image => {
    return {
        type: ADD_IMAGE,
        image
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
    const res = await fetch(`/api/memories/${memId}/`)

    if (res.ok) {
        const mem = await res.json()
        dispatch(getOneMemory(mem))
        return mem
    }
}

export const fetchCreateMemory = (memory) => async (dispatch) => {
    const res = await fetch('/api/memories/new/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(memory)
    })

    if (res.ok) {
        const newMem = await res.json()
        dispatch(createMemory(newMem))
        return newMem
    }
}

export const fetchAddImage = (image) => async (dispatch) => {
    const res = await fetch('/api/memories/new/image/', {
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
