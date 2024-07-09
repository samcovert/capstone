import { useDispatch, useSelector } from "react-redux"
import { NavLink } from "react-router-dom"
import './history.css'
import { useEffect } from "react"
import { fetchAllTeams } from "../../redux/teams"


const History = () => {
    const dispatch = useDispatch()
    const teams = useSelector(state => state.teams)

    useEffect(() => {
        dispatch(fetchAllTeams())
    }, [dispatch])

    return (
        <>
        <h1>Coyotes Franchise History</h1>
        <div className="years">
        <NavLink className='team-year'>1996-97</NavLink>
        <NavLink className='team-year'>1997-98</NavLink>
        <NavLink className='team-year'>1998-99</NavLink>
        <NavLink className='team-year'>1999-00</NavLink>
        <NavLink className='team-year'>2000-01</NavLink>
        <NavLink className='team-year'>2001-02</NavLink>
        <NavLink className='team-year'>2002-03</NavLink>
        <NavLink className='team-year'>2003-04</NavLink>
        <NavLink className='team-year'>2004-05</NavLink>
        <NavLink className='team-year'>2005-06</NavLink>
        <NavLink className='team-year'>2006-07</NavLink>
        <NavLink className='team-year'>2007-08</NavLink>
        <NavLink className='team-year'>2008-09</NavLink>
        <NavLink className='team-year'>2010-11</NavLink>
        <NavLink className='team-year'>2011-12</NavLink>
        <NavLink className='team-year'>2012-13</NavLink>
        <NavLink className='team-year'>2013-14</NavLink>
        <NavLink className='team-year'>2014-15</NavLink>
        <NavLink className='team-year'>2015-16</NavLink>
        <NavLink className='team-year'>2016-17</NavLink>
        <NavLink className='team-year'>2017-18</NavLink>
        <NavLink className='team-year'>2018-19</NavLink>
        <NavLink className='team-year'>2019-20</NavLink>
        <NavLink className='team-year'>2020-21</NavLink>
        <NavLink className='team-year'>2021-22</NavLink>
        <NavLink className='team-year'>2022-23</NavLink>
        <NavLink className='team-year'>2023-24</NavLink>
        </div>
        </>
    )
}

export default History
