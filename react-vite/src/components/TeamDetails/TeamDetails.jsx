import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { fetchTeamDetails } from "../../redux/teams"


const TeamDetails = () => {
    const { teamYear } = useParams()
    const dispatch = useDispatch()
    const teams = useSelector(state => state.teams)
    const team = teams ? Object.values(teams).find(team => team.year === teamYear) : undefined

    useEffect(() => {
        if (!team) {
            dispatch(fetchTeamDetails(teamYear))
        }
    }, [dispatch, teamYear, team])

    if (!teams) {
        return <div>Loading teams...</div>
    }

    if (!team) {
        return <div>Loading team details...</div>
    }

    return (
        <>
        {team.players.map(player => (
            <div key={player.id}>
                <span>{player.first_name}</span>
                <span>{player.last_name}</span>
                <span>{player.position}</span>
                <span>{player.goals}</span>
                <span>{player.assists}</span>
                <span>{player.points}</span>
                <span>{player.pims}</span>
                <span>{player.plus_minus}</span>
                <span>{player.gaa}</span>
                <span>{player.wins}</span>
                <span>{player.svp}</span>
                <span>{player.gp}</span>
                <span>{player.age}</span>
            </div>
        ))}
        </>
    )
}

export default TeamDetails
