import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom"
import './history.css'
import { useEffect } from "react"
import { fetchAllTeams } from "../../redux/teams"


const History = () => {
    const dispatch = useDispatch()
    const teams = useSelector(state => Object.values(state.teams))

    useEffect(() => {
        dispatch(fetchAllTeams())
    }, [dispatch])

    return (
        <>
        <h1 className="history-title">Coyotes Franchise History</h1>
        <div className="history-sub">
            Click on any of these years to see details about how the Coyotes did that season including
            the teams record, player stats, the head coach, and more.
        </div>
        <div className="history-teams">
            {teams.map(team => (
                <NavLink key={team.id} to={`/history/${team.year}/`} className='history-team-year'>
                    {team.year}
                </NavLink>
            ))}
        </div>
        </>
    )
}

export default History
