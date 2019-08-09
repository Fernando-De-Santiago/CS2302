import * as THREE from 'three';
import OrbitControls from 'three-orbitcontrols';
var scene = new THREE.Scene();
			var far = 5;
			var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, far);
			
			var renderer = new THREE.WebGLRenderer();
			//renderer.setClearColor(0x333333);
			renderer.setClearColor(0xffffff);
			renderer.shadowMap.enabled = true;
			//renderer.shadowMap.type = THREE.PCFShadowMap;
			renderer.shadowMap.type = THREE.PCFSoftShadowMap;
			


			var controls = new OrbitControls( camera, renderer.domElement );
			renderer.setSize( window.innerWidth/3, window.innerHeight/2 );
			document.body.appendChild( renderer.domElement );

			var geometry = new THREE.BoxGeometry( 1, 1, 1 );
			var material = new THREE.MeshPhongMaterial( { color: 0x44aa88 } );
			var cube = new THREE.Mesh( geometry, material );


			//create floors stage
			var geometry2 = new THREE.BoxGeometry( 10, 10, 10 );
			var material2 = new THREE.MeshPhongMaterial( { color: 0xffffff } );
			var floor = new THREE.Mesh(geometry2,material2);
			// floor.rotation.x = -90 *(Math.pi/180);
			// floor.rotation.y = -100;
			scene.add(floor);

			

			//sets the background color
			scene.background = new THREE.Color(0x808080);
			scene.add( cube );
			camera.position.z = 5;
			//camera.position.set( 0, 20, 100 );
			controls.update();


			//adds spotlight
			var spotLight = new THREE.SpotLight( 0xff0000);
			spotLight.position.y = 10;
			spotLight.target = cube;
			spotLight.castShadow= true;
			spotLight.shadow = new THREE.LightShadow(new THREE.PerspectiveCamera(100,1,500,1000));
			spotLight.shadow.bias = .001;
			//spotLight.shadow.mapSize
			cube.castShadow = true;


			//adds dirctional light
			var light = new THREE.AmbientLight( 0x404040 ); // soft white light
			scene.add( light );
			var directionalLight = new THREE.DirectionalLight( 0xffffff, .8 );
			scene.add( directionalLight.cube );
			//target

			directionalLight.castShadow = true;
			directionalLight.target= cube ;

			var ptLight = new THREE.PointLight(0xffffff,1.0,600);
			scene.add(ptLight);
			scene.add( directionalLight );

			
			

			var animate = function () {
				requestAnimationFrame( animate );

				// cube.rotation.x += 0.01;
				// cube.rotation.y += 0.01;
				
				renderer.render( scene, camera );
			};
			

		
			
			animate();
