import React from "react";
import Link from "next/link";

const Navbar = () => {
  return (
    <div>
      <div>
        <Link href="/">
          <h1>VisionCraft</h1>
        </Link>
        <ul>
          <li>
            <Link href="/">Home</Link>
          </li>
          <li>
            <Link href="/generate">Generate</Link>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
