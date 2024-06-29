import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import Merchandise from '../components/Merchandise';
import MerchDetails from '../components/MerchDetails';
import CreateMerch from '../components/CreateMerch';
import UpdateMerch from '../components/CreateMerch/UpdateMerch';
import UserProfile from '../components/UserProfile';
import News from '../components/News';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <h1>Welcome!</h1>,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "merch",
        element: <Merchandise />
      },
      {
        path: "merch/:merchId",
        element: <MerchDetails />
      },
      {
        path: "merch/new",
        element: <CreateMerch />
      },
      {
        path: "merch/:merchId/edit",
        element: <UpdateMerch />
      },
      {
        path: "user/profile",
        element: <UserProfile />
      },
      {
        path: 'news',
        element: <News />
      }
    ],
  },
]);
