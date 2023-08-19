import React from "react";
import { Card, CardHeader, CardBody, CardFooter } from "@nextui-org/react";
import Image from "next/image";

export default function Info() {
  const list = [
    {
      title: "Identify",
      img: "/image1.png",
      description: "Identify",
    },
    {
      title: "Identify",
      img: "/image2.png",
      description: "Identify",
    },
    {
      title: "Identify",
      img: "/image3.png",
      description: "Identify",
    },
  ];
  return (
    <div className="flex flex-col items-center justify-center h-screen mb-12 bg-fixed bg-center bg-cover custom-img">
      <div className="text-center z-10">
        <h2 className="text-2xl font-bold p-6 text-sky-500">Identify</h2>

        <h1 className="text-5xl w-2/3 break-normal mx-auto mb-10 p-6 font-extrabold">
          Upload any image and we find what you can use
        </h1>
      </div>
      <div className="gap-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
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
            <CardFooter className="text-small justify-between">
              <b>{item.title}</b>
              <p className="text-default-500">{item.price}</p>
            </CardFooter>
          </Card>
        ))}
      </div>
    </div>
  );
}
