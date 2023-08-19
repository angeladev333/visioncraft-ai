import React from "react";
import Link from "next/link";
import { Typewriter } from "react-simple-typewriter";

export const Hero = () => {
  return (
    <div className="flex items-center justify-center h-screen mb-12 bg-fixed bg-center bg-cover custom-img">
      <div className="text-center z-10">
        <h2 className="text-2xl font-bold p-6 bg-clip-text text-transparent bg-gradient-to-t from-pink-500 to-blue-400">
          Announcing VisionCraft →
        </h2>

        <h1 className="text-8xl font-extrabold">Your Toolbox,</h1>
        <h1 className="text-8xl font-extrabold p-6 text-violet-600">
          <span className="bg-violet-400 bg-opacity-50 p-2 inline-block">
            Our{" "}
            <Typewriter
              words={["Playground.", "Vision.", "Canvas."]}
              loop={10}
              cursor
              cursorStyle="|"
              typeSpeed={70}
              deleteSpeed={80}
              delaySpeed={3000}
            />
          </span>
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
