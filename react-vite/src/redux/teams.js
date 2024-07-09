const GET_ALL_TEAMS = '/teams/GET_ALL_TEAMS'
const GET_TEAM_DETAILS = '/teams/GET_TEAM_DETAILS'

const getAllTeams = teams => {
    return {
        type: GET_ALL_TEAMS,
        teams
    }
}

const getTeamDetails = team => {
    return {
        type: GET_TEAM_DETAILS,
        team
    }
}

export const fetchAllTeams = () => async (dispatch) => {
    const res = await fetch('/api/history/teams/')

    if (res.ok) {
        const teams = await res.json()
        dispatch(getAllTeams(teams))
        return teams
    }
}

export const fetchTeamDetails = (year) => async (dispatch) => {
    const res = await fetch(`/api/history/teams/${year}/`)

    if (res.ok) {
        const team = await res.json()
        dispatch(getTeamDetails(team))
        return team
    }
}

const initialState = {}
const teamsReducer = (state=initialState, action) => {
    switch (action.type) {
        case GET_ALL_TEAMS: {
            const newState = { ...state }
            action.teams.forEach(team => (newState[team.id] = team))
            return newState
        }
        case GET_TEAM_DETAILS: {

            return {
                ...state,
                [action.team.year]: action.team
            }
        }
        default:
            return state
    }
}

export default teamsReducer
