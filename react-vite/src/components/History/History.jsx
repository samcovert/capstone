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
console.log(teams)
    return (
        <>
        <h1>Coyotes Franchise History</h1>
        <div className="years">
            {teams.map(team => (
                <NavLink key={team.id} to={`/history/${team.year}/`} className='team-year'>{team.year}</NavLink>
            ))}
        </div>
        </>
    )
}

export default History
