import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";


function Navigation() {
  return (
    <>
    <div className="nav-bar">
        <NavLink to="/">
          <img className="logo" src="/logo-yotes-4-ever.png"></img>
        </NavLink>
        <p className="slogan">Hockey Belongs In The Desert</p>
        <ProfileButton />
    </div>
    <div className="nav-bottom">
        <NavLink className='nav-item' to='/merch'>Store</NavLink>
        <NavLink className='nav-item' to='/news'>News</NavLink>
        <NavLink className='nav-item' to='/history'>History</NavLink>
        <NavLink className='nav-item' to='/memories'>Memories</NavLink>
    </div>
    </>
  );
}

export default Navigation;
