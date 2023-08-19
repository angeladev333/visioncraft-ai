import Link from "next/link";

const Navbar = () => {
  return (
    <div className="navbar-wrapper">
      <div>
        <Link className="rightlink" href="/" passHref>
          OP Company
        </Link>
      </div>
      <div className="leftlink-wrapper">
        <Link className="leftlink" href="/about" passHref>
          about
        </Link>
      </div>
    </div>
  );
};

export default Navbar;
