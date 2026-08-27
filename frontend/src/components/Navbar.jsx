import { Bell, Search, User } from "lucide-react";

function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-left">
        <h2>JANSETU AI</h2>
      </div>

      <div className="navbar-search">
        <Search size={18} />
        <input
          type="text"
          placeholder="Search challenges..."
        />
      </div>

      <div className="navbar-right">
        <button className="icon-button">
          <Bell size={20} />
        </button>

        <div className="user-profile">
          <div className="user-avatar">
            <User size={18} />
          </div>

          <div>
            <strong>Citizen</strong>
            <span>Community Member</span>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Navbar;