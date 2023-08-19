import React, { useState, useEffect } from "react";
import Link from "next/link";

const Navbar = () => {
  const [color, setColor] = useState("transparent");
  const [textColor, setTextColor] = useState("black");

  useEffect(() => {
    const changeColor = () => {
      if (window.scrollY >= 90) {
        setColor("linear-gradient(to bottom, #5485B7, transparent)");
        setTextColor("white");
      } else {
        setColor("transparent");
        setTextColor("black");
      }
    };
    window.addEventListener("scroll", changeColor);
  });

  return (
    <div
      style={{ background: `${color}` }}
      className="fixed left-0 top-0 w-full z-10 ease-in duration-300"
    >
      <div className="max-w-[1240px] m-auto flex justify-between items-center p-4">
        <Link href="/">
          <h1 style={{ color: `${textColor}` }} className="font-bold text-3xl">
            VisionCraft
          </h1>
        </Link>
        <ul style={{ color: `${textColor}` }} className="flex">
          <li className="p-2 hover:text-gray-500">
            <Link href="/">Home</Link>
          </li>

          <li className="px-10 m-auto hover:text-gray-500">
            <Link href="/generate">
              <button className="p-2 w-40 h-10 text-white button-gradient rounded-full">
                Get Started
              </button>
            </Link>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
