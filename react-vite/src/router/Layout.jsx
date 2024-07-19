import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";
import '../index.css'

export default function Layout() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <ModalProvider>
        <Navigation />
        {isLoaded &&
        <>
        <div className="layout">
        <Outlet />
        <img src="https://samsclub13.s3.us-west-2.amazonaws.com/background.jpeg" className="background-logo" />
        <div className="background"></div>
        </div>

        </>}
        <Modal />
      </ModalProvider>
    </>
  );
}
