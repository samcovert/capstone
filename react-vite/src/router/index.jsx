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
import NewsDetails from '../components/NewsDetails';
import Homepage from '../components/Homepage';
import CreateNews from '../components/CreateNews';
import UpdateNews from '../components/CreateNews/UpdateNews';
import History from '../components/History';
import TeamDetails from '../components/TeamDetails/TeamDetails';
import Memories from '../components/Memories';
import MemoryDetails from '../components/MemoryDetails';
import CreateMemory from '../components/CreateMemory';
import UpdateMemory from '../components/CreateMemory/UpdateMemory';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Homepage />,
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
      },
      {
        path: 'news/:newsId',
        element: <NewsDetails />
      },
      {
        path: 'news/new',
        element: <CreateNews />
      },
      {
        path: 'news/:newsId/edit',
        element: <UpdateNews />
      },
      {
        path: 'history',
        element: <History />
      },
      {
        path: 'history/:teamYear',
        element: <TeamDetails />
      },
      {
        path: 'memories',
        element: <Memories />
      },
      {
        path: 'memories/:memoryId',
        element: <MemoryDetails />
      },
      {
        path: 'memories/new',
        element: <CreateMemory />
      },
      {
        path: 'memories/:memoryId/edit',
        element: <UpdateMemory />
      }
    ],
  },
]);
