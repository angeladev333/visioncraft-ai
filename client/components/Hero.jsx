import React from "react";

export const Hero = () => {
  return (
    <div className="flex items-center justify-center h-screen">
      <div />
      <div className="text-center mt-[-10rem]">
        <h1 className="text-6xl font-extrabold p-5">
          Your Toolbox, Our Canvas
        </h1>
        <p className="text-xl">
          VisionCraft is a new way to capture and analyze your hardware setup,
          unlocking a wealth of possibilities
        </p>
        <button className="font-medium px-4 py-2 mt-4 text-white bg-sky-500 rounded-full hover:bg-sky-600">
          Get Started
        </button>
      </div>
    </div>
  );
};
