import test from "node:test";
import assert from "node:assert/strict";
import { primeSieve, goldbachPairs, bounded, ulamPoints } from "../src/lib/primes.ts";

test("sieve agrees with independent trial division across the experiment range", () => {
  const prime = primeSieve(2000);
  for (let n=0;n<=2000;n++) {
    let expected=n>=2;
    for(let d=2;d*d<=n;d++) if(n%d===0){expected=false;break;}
    assert.equal(Boolean(prime[n]),expected,`n=${n}`);
  }
});

test("pairs include repeated primes, reject invalid input, and match independent enumeration", () => {
  const prime=primeSieve(2000);
  assert.deepEqual(goldbachPairs(4,prime),[[2,2]]);
  assert.deepEqual(goldbachPairs(10,prime),[[3,7],[5,5]]);
  assert.deepEqual(goldbachPairs(100,prime),[[3,97],[11,89],[17,83],[29,71],[41,59],[47,53]]);
  for(const n of [2,5,4.5,2002,NaN]) assert.deepEqual(goldbachPairs(n,prime),[]);
  const isPrime=(n:number)=>{if(n<2)return false;for(let d=2;d*d<=n;d++)if(n%d===0)return false;return true;};
  for(let n=4;n<=2000;n+=2) {
    const expected=[];
    for(let p=2;p<=n/2;p++)if(isPrime(p)&&isPrime(n-p))expected.push([p,n-p]);
    assert.deepEqual(goldbachPairs(n,prime),expected,`n=${n}`);
    assert.ok(expected.length>0);
  }
});

test("bounded coordinates stay inside endpoints and preserve midpoint reflection", () => {
  for(const s of [1,20,200])for(const m of [2,50,1000])for(const d of [0,1,20]) {
    assert.ok(Math.abs(bounded(m+d,s,m))<1);
    assert.equal(bounded(m+d,s,m)+bounded(m-d,s,m),0);
  }
  assert.notEqual(bounded(3,20)+bounded(97,20),2*bounded(50,20));
});

test("Ulam spiral assigns known positions and unique prime locations", () => {
  const points=ulamPoints(49), prime=primeSieve(2401);
  assert.deepEqual(points.slice(0,4),[{n:2,x:1,y:0},{n:3,x:1,y:-1},{n:5,x:-1,y:-1},{n:7,x:-1,y:1}]);
  assert.equal(points.length,Array.from(prime).filter(Boolean).length);
  assert.equal(new Set(points.map(p=>`${p.x},${p.y}`)).size,points.length);
  assert.ok(points.every(p=>Math.abs(p.x)<=24&&Math.abs(p.y)<=24));
});
