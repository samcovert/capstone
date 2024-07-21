import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from "react-router-dom"
import { fetchTeamDetails } from "../../redux/teams"
import './TeamDetails.css'


const TeamDetails = () => {
    const { teamYear } = useParams()
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const teams = useSelector(state => state.teams)
    const team = teams ? Object.values(teams).find(team => team.year === teamYear) : undefined
    const forwards = team?.players.filter(player => player.position === 'C' || player.position === 'R' || player.position === 'L')
    const defense = team?.players.filter(player => player.position === 'D')
    const goalies = team?.players.filter(player => player.position === 'G')

    useEffect(() => {
        if (!team) {
            dispatch(fetchTeamDetails(teamYear))
        }
    }, [dispatch, teamYear, team])

    const handleBack = () => {
        navigate('/history')
    }

    if (!teams) {
        return <div>Loading teams...</div>
    }

    if (!team) {
        return <div>Loading team details...</div>
    }

    return (
        <>
            <div onClick={handleBack} className="back-button">Back to History</div>
            <h1 className="team-name">{team.team_name}</h1>
            <h2 className="team-year">{team.year} {`(${team.record})`}</h2>
            <div className="team-facts">
                <div className="team-fact">Playoffs: {team.playoffs}</div>
                <div className="team-fact">Head Coach: {team.coach}</div>
            </div>
            <div className="player-stats">
                <h3 className="position">Forwards</h3>
                <div className="player-stats-header forwards-header">
                    <span>Name</span>
                    <span>Number</span>
                    <span>Position</span>
                    <span>Goals</span>
                    <span>Assists</span>
                    <span>Points</span>
                    <span>PIMs</span>
                    <span>+/-</span>
                    <span>GP</span>
                    <span>Age</span>
                </div>
                {forwards.map(player => (
                    <div key={player.id} className="player-stat forwards-stat">
                        <span>{player.first_name} {player.last_name}</span>
                        <span>{player.number}</span>
                        <span>{player.position}</span>
                        <span>{player.goals}</span>
                        <span>{player.assists}</span>
                        <span>{player.points}</span>
                        <span>{player.pims}</span>
                        <span>{player.plus_minus}</span>
                        <span>{player.gp}</span>
                        <span>{player.age}</span>
                    </div>
                ))}

                <h3 className="position">Defensemen</h3>
                <div className="player-stats-header defense-header">
                    <span>Name</span>
                    <span>Number</span>
                    <span>Position</span>
                    <span>Goals</span>
                    <span>Assists</span>
                    <span>Points</span>
                    <span>PIMs</span>
                    <span>+/-</span>
                    <span>GP</span>
                    <span>Age</span>
                </div>
                {defense.map(player => (
                    <div key={player.id} className="player-stat defense-stat">
                        <span>{player.first_name} {player.last_name}</span>
                        <span>{player.number}</span>
                        <span>{player.position}</span>
                        <span>{player.goals}</span>
                        <span>{player.assists}</span>
                        <span>{player.points}</span>
                        <span>{player.pims}</span>
                        <span>{player.plus_minus}</span>
                        <span>{player.gp}</span>
                        <span>{player.age}</span>
                    </div>
                ))}

                <h3 className="position">Goalies</h3>
                <div className="player-stats-header goalies-header">
                    <span>Name</span>
                    <span>Number</span>
                    <span>GAA</span>
                    <span>SV%</span>
                    <span>Wins</span>
                    <span>GP</span>
                    <span>Age</span>
                </div>
                {goalies.map(player => (
                    <div key={player.id} className="player-stat goalies-stat">
                        <span>{player.first_name} {player.last_name}</span>
                        <span>{player.number}</span>
                        <span>{player.gaa}</span>
                        <span>{player.svp}</span>
                        <span>{player.wins}</span>
                        <span>{player.gp}</span>
                        <span>{player.age}</span>
                    </div>
                ))}
            </div>
        </>
    )
}

export default TeamDetails
