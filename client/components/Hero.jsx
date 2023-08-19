import React from "react";
import Link from "next/link";

export const Hero = () => {
  return (
    <div className="flex items-center justify-center h-screen">
      <div />
      <div className="text-center mt-[-5rem]">
        <h1 className="text-6xl font-extrabold p-6">
          Your Toolbox, Our Canvas
        </h1>
        <p className="text-2xl w-2/3 break-normal mx-auto p-6">
          VisionCraft is a new way to capture and analyze your hardware setup,
          unlocking a wealth of possibilities
        </p>
        <Link href="/generate">
          <button className="text-2xl font-medium px-4 py-2 mt-10 w-60 h-14 text-white button-gradient rounded-full">
            Get Started
          </button>
        </Link>
      </div>
    </div>
  );
};
