function moebiusTransform(point, circleRadius = 1, p = 0, q = 1, t = 0.5) {
    // Normalize point to unit circle
    const [xa, ya, za] = point.map(coord => coord / circleRadius);

    // Reverse stereographic projection to 4D hypersphere
    const denom = 1 + xa * xa + ya * ya + za * za;
    const xb = 2 * xa / denom;
    const yb = 2 * ya / denom;
    const zb = 2 * za / denom;
    const wb = (-1 + xa * xa + ya * ya + za * za) / denom;

    // Rotate hypersphere by amount t
    const xc = (xb) * (Math.cos(p * t)) + (yb) * (Math.sin(p * t));
    const yc = -(xb) * (Math.sin(p * t)) + (yb) * (Math.cos(p * t));
    const zc = (zb) * (Math.cos(q * t)) - (wb) * (Math.sin(q * t));
    const wc = (zb) * (Math.sin(q * t)) + (wb) * (Math.cos(q * t));

    // Project stereographically back to flat 3D
    const xd = xc / (1 - wc);
    const yd = yc / (1 - wc);
    const zd = zc / (1 - wc);

    // Transform back to input circle
    const transformedPoint = [xd * circleRadius, yd * circleRadius, zd * circleRadius];

    return transformedPoint;
}

// Example usage
const inputPoint = [0.5, 0.5, 0.5];  // Point in 3D space
const transformedPoint = moebiusTransform(inputPoint, 1, 0, 1, 0.5);
console.log("Transformed Point:", transformedPoint);
