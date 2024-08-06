import './Homepage.css'

const Homepage = () => {
    return (
        <>
        <div className="homepage-container">
        <h1 className="home-title">Gone But Never Forgotten</h1>
        <h4 className="home-sub">In memory of the Phoenix/Arizona Coyotes</h4>
        <p className="home-description">Yotes 4 Ever is dedicated to keeping the memory of the
            Phoenix/Arizona Coyotes alive. Click the hockey sticks to create a profile and join
             the Coyotes Community in buying/selling items, sharing news, and keeping memories of our beloved Desert Dawgs.
        </p>
        </div>
        <footer className="home-footer">
                <div className="footer-content">
                    <div className="created-by">
                        Created By Sam Covert
                    </div>
                    <div className="footer-links">
                        <a href="https://github.com/samcovert" target="_blank" rel="noopener noreferrer" className="footer-link">GitHub</a>
                        <a href="https://www.linkedin.com/in/sam-covert-3b1482321/" target="_blank" rel="noopener noreferrer" className="footer-link">LinkedIn</a>
                    </div>
                </div>
            </footer>
        </>
    )
}

export default Homepage
