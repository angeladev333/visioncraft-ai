import React from "react";
import Link from "next/link";

// const Navbar = () => {
//   return (
//     <div className="navbar-wrapper">
//       <div>
//         <Link className="rightlink" href="/" passHref>
//           OP Company
//         </Link>
//       </div>
//       <div className="leftlink-wrapper">
//         <Link className="leftlink" href="/about" passHref>
//           about
//         </Link>
//       </div>
//     </div>
//   );
// };

const Navbar = () => {
  return (
    <ul>
      <li>
        <Link href="/">Home</Link>
      </li>
      <li>
        <Link href="/about">About</Link>
      </li>
    </ul>
  );
};

export default Navbar;
