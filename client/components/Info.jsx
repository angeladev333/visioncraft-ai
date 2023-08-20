import React from "react";
import { Card, CardHeader, CardBody, CardFooter } from "@nextui-org/react";
import Image from "next/image";

export default function Info() {
  const list = [
    {
      img: "/image1.png",
    },
    {
      img: "/image2.png",
    },
    {
      img: "/image3.png",
    },
  ];



  return (
    <div className="flex flex-col items-center justify-center h-screen mb-12 bg-fixed bg-center bg-cover custom-img">
      <div className="text-center z-10">
      <div className="bg-white p-4 rounded shadow-md rounded-3xl">
        <h2 className="text-4xl font-bold p-6 text-violet-500">BUILD</h2>

        <h1 className="text-5xl w-2/3 break-normal mx-auto mb-10 p-6 font-extrabold">
          Upload any image and we'll find what you can create
        </h1>
      
      
      <div className="px-60 gap-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
        {list.map((item, index) => (
          <Card
            shadow="sm"
            key={index}
            isPressable
            onPress={() => console.log("item pressed")}
            className="p-0"
            

          >
            <CardBody className="p-0">
              {" "}
              <Image
                width={2400}
                height={2400}
                alt={item.title}
                className="w-full h-full object-cover"
                src={item.img}
                
              />
            </CardBody>
            
          </Card>
        ))}
          </div>
        </div>
      </div>
    </div>
  );
}

