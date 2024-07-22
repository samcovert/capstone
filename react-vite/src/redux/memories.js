const GET_ALL_MEMORIES = '/memories/GET_ALL_MEMORIES'
const GET_ONE_MEM = '/memories/GET_ONE_MEM'
const CREATE_MEMORY = '/memories/CREATE_MEMORY'
const ADD_IMAGE = '/memories/ADD_IMAGE'
const EDIT_MEMORY = '/memories/EDIT_MEMORY'
const EDIT_IMAGE = '/memories/EDIT_IMAGE'
const DELETE_MEMORY = '/memories/DELETE_MEMORY'
const ADD_COMMENT = '/memories/ADD_COMMENT'
const EDIT_COMMENT = '/memories/EDIT_COMMENT'
const DELETE_COMMENT = '/memories/DELETE_COMMENT'
const ADD_LIKE = '/memories/ADD_LIKE'
const REMOVE_LIKE = '/memories/REMOVE_LIKE'

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

const editMemory = memory => {
    return {
        type: EDIT_MEMORY,
        memory
    }
}

const editImage = image => {
    return {
        type: EDIT_IMAGE,
        image
    }
}

const deleteMemory = memoryId => {
    return {
        type: DELETE_MEMORY,
        memoryId
    }
}

const addComment = comment => {
    return {
        type: ADD_COMMENT,
        comment
    }
}

const editComment = comment => {
    return {
        type: EDIT_COMMENT,
        comment
    }
}

const deleteComment = (commentId, memoryId) => {
    return {
        type: DELETE_COMMENT,
        commentId,
        memoryId
    }
}

const addLike = memory => {
    return {
        type: ADD_LIKE,
        memory
    }
}

const removeLike = (id, memoryId) => {
    return {
        type: REMOVE_LIKE,
        id,
        memoryId
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
        dispatch(fetchOneMemory(newImage.id))
        return newImage
    }
}

export const fetchEditMemory = (memory, memId) => async (dispatch) => {
    const res = await fetch(`/api/memories/${memId}/edit/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(memory)
    })

    if (res.ok) {
        const updatedMem = await res.json()
        dispatch(editMemory(updatedMem))
        dispatch(fetchOneMemory(memId))
        return updatedMem
    }
}

export const fetchEditImage = ({ url, memory_id, image_id }) => async (dispatch) => {
    try {
        const res = await fetch(`/api/memories/${image_id}/images/edit/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url })
        });

        if (!res.ok) {
            const errorData = await res.json();
            console.error("Error updating image:", errorData);
            return;
        }

        const updatedImage = await res.json();
        dispatch(editImage(updatedImage));
        dispatch(fetchOneMemory(memory_id));
        return updatedImage;
    } catch (error) {
        console.error("Fetch error:", error);
    }
}

export const fetchDeleteMemory = (memoryId) => async (dispatch) => {
    const res = await fetch(`/api/memories/${memoryId}/delete/`, {
        method: 'DELETE'
    })
    if (res.ok) {
        dispatch(deleteMemory(memoryId))
        return
    }
}

export const fetchAddComment = (comment) => async (dispatch) => {
    const res = await fetch('/api/memories/comment/new/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(comment)
    })
    if (res.ok) {
        const newComment = await res.json()
        dispatch(addComment(newComment))
        return newComment
    }
}

export const fetchEditComment = (comment, commentId, memoryId) => async (dispatch) => {
    const res = await fetch(`/api/memories/${commentId}/comment/edit/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(comment)
    })
    if (res.ok) {
        const updatedComment = await res.json()
        dispatch(editComment(updatedComment))
        dispatch(fetchOneMemory(memoryId))
        return updatedComment
    }
}

export const fetchDeleteComment = (commentId, memoryId) => async (dispatch) => {
    const res = await fetch(`/api/memories/${commentId}/comment/delete/`, {
        method: 'DELETE'
    })
    if (res.ok) {
        dispatch(deleteComment(commentId))
        dispatch(fetchOneMemory(memoryId))
        return
    }
}

export const fetchAddLike = (memoryId) => async (dispatch) => {
    const res = await fetch(`/api/memories/${memoryId}/like/`, {
        method: 'POST'
    })
    if (res.ok) {
        const updatedMem = await res.json()
        dispatch(addLike(updatedMem))
        return updatedMem
    }
}

export const fetchDeleteLike = (id, memoryId) => async (dispatch) => {
    const res = await fetch(`/api/memories/${id}/like/delete/`, {
        method: 'DELETE'
    })
    if (res.ok) {
        dispatch(removeLike(id, memoryId))
        return
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
        case CREATE_MEMORY: {
            const newState = {
                ...state,
                [action.memory.id]: action.memory
            }
            return newState
        }
        case ADD_IMAGE: {
            const newState = { ...state }
            const mem = newState[action.image.memory_id]
            if (mem) {
                mem.images = mem.images ? [...mem.images, action.image] : [action.image]
            }
            return newState
        }
        case EDIT_MEMORY: {
            return {
                ...state,
                [action.memory.id]: action.memory
            }
        } case EDIT_IMAGE: {
            const newState = { ...state }
            const mem = newState[action.image.memory_id]
            if (mem) {
                mem.images = mem.images.map(img => img.id === action.image.id ? action.image : img)
            }
            return newState
        } case DELETE_MEMORY: {
            const newState = { ...state }
            delete newState[action.memoryId]
            return newState
        }
        case ADD_COMMENT: {
            const newState = { ...state }
            const mem = newState[action.comment.mem_id]
            if (mem) {
                mem.comments = [...mem.comments, action.comment]
            }
            return newState
        }
        case EDIT_COMMENT: {
            const newState = { ...state }
            const mem = newState[action.comment.memory_id]
            if (mem) {
                mem.comments = mem.comments.map(comment =>
                    comment.id === action.comment.id ? action.comment : comment
                )
            }
            return newState
        }
        case DELETE_COMMENT: {
            const newState = { ...state }
            const mem = newState[action.memoryId]
            if (mem) {
                mem.comments = mem.comments.filter(comment => comment.id !== action.commentId)
            }
            return newState
        }
        case ADD_LIKE: {
            return {
                ...state,
                [action.memory.id]: action.memory
            }
        }
        case REMOVE_LIKE: {
            const newState = { ...state }
            const mem = { ...newState[action.memoryId] }
            if (mem) {
                mem.user_likes = mem.user_likes.filter(like => like.id !== action.id)
                mem.likes -= 1
                newState[action.memoryId] = mem
            }
            return newState
        }
        default:
            return state
    }
}

export default memsReducer
