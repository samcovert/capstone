import { useDispatch, useSelector } from 'react-redux';
import './Merchandise.css';
import { useEffect, useState } from 'react';
import { fetchAllMerch } from '../../redux/merch';
import { Link, useNavigate } from 'react-router-dom';
import LoginFormModal from '../LoginFormModal';
import OpenModalButton from '../OpenModalButton/OpenModalButton';

const Merchandise = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate()
    const merchandise = useSelector(state => Object.values(state.merchandise));
    const user = useSelector(state => state.session.user);
    const [currentIndexes, setCurrentIndexes] = useState({});

    useEffect(() => {
        dispatch(fetchAllMerch());
    }, [dispatch]);

    useEffect(() => {
        if (merchandise.length > 0) {
            const initialIndexes = {};
            merchandise.forEach(item => {
                if (!(item.id in currentIndexes)) {
                    initialIndexes[item.id] = 0;
                }
            });
            if (Object.keys(initialIndexes).length > 0) {
                setCurrentIndexes(prev => ({ ...prev, ...initialIndexes }));
            }
        }
    }, [merchandise, currentIndexes]);


    const handlePrev = (id, length) => {
        setCurrentIndexes(prev => ({
            ...prev,
            [id]: (prev[id] - 1 + length) % length
        }));
    };

    const handleNext = (id, length) => {
        setCurrentIndexes(prev => ({
            ...prev,
            [id]: (prev[id] + 1) % length
        }));
    };

    if (!merchandise) {
        return <h1>Loading...</h1>
    }

    return (
        <>
        <div className='merch-page-container'>
            <h1 className='merch-title'>Welcome to the Coyotes Merch Store!</h1>
            <h2 className='merch-subtitle'>Sell your old Coyotes merchandise, or buy things other fans are selling.</h2>
            {user ? (
                    <button className='sell-button' onClick={() => navigate('/merch/new')}>Add an item to sell</button>
            ) : (
                <OpenModalButton
                    buttonText='Sign in to get started'
                    modalComponent={<LoginFormModal />}
                />
            )}
            <div className='merch-item-container'>
                {merchandise?.map(merch => (
                    <div key={merch.id} className="merch-card">
                        <div className='merch-card-user'>Seller: {merch.user.username}</div>
                        <div className="carousel">
                    <Link to={`/merch/${merch.id}`}>
                            {merch.images?.map((image, index) => (
                                <div
                                    key={index}
                                    className={`carousel-item ${currentIndexes[merch.id] === index ? 'active' : ''}`}
                                >
                                    <img className="merch-image" src={image.url} alt={merch.name} />
                                </div>
                            ))}
                    </Link>
                            {merch.images?.length > 1 &&
                            <>
                            <button className="carousel-arrow left" onClick={() => handlePrev(merch.id, merch.images.length)}>{'<'}</button>
                            <button className="carousel-arrow right" onClick={() => handleNext(merch.id, merch.images.length)}>{'>'}</button>
                            </>
                            }
                        </div>
                        <div className='merch-card-bottom'>
                        <Link to={`/merch/${merch.id}`} className='merch-card-links'>
                            <div className='merch-name'>
                                {merch.name}
                            </div>
                        </Link>
                        </div>
                    </div>
                ))}
            </div>
            </div>
        </>
    );
};

export default Merchandise
